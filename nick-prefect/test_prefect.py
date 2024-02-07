import httpx
import pydantic
from typing import Dict, Union
from prefect import flow, task, get_run_logger


class Repo(pydantic.BaseModel):
    name: str
    stargazers_count: int
    forks_count: int

    # Ignore unrecognized fields
    class Config:
        extra = "ignore"


class Response(pydantic.BaseModel):
    repo: Union[Repo, None]
    error: Union[str, None]


@task
def get_url(url: str, params: dict = None) -> Dict:
    """Get the JSON response from a URL.

    Args:
        url (str): _description_
        params (dict, optional): _description_. Defaults to None.

    Returns:
        Dict: Response JSON
    """
    try:
        # Get the response
        response = httpx.get(url, params=params)
        response.raise_for_status()

        # Cast to models and return
        repo: Repo = Repo(**response.json())
        return Response(repo=repo, error=None)
    except httpx.HTTPError as e:
        return Response(repo=None, error=str(e))


@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    """Get the statistics of a GitHub repository.

    Args:
        repo_name (str, optional): _description_. Defaults to "PrefectHQ/prefect".
    """
    # Get logger
    logger = get_run_logger()

    # Get the repository information
    url = f"https://api.github.com/repos/{repo_name}"
    response: Response = get_url(url)

    # Log the statistics
    if response.error:
        logger.error(f"Failed to get repository information: {response.error}")
        return False
    else:
        logger.info("PrefectHQ/prefect repository statistics 🤓:")
        logger.info(f"Stars 🌠 : {response.repo.stargazers_count}")
        logger.info(f"Forks 🍴 : {response.repo.forks_count}")
        return True


def parse_args():
    import argparse

    parser = argparse.ArgumentParser(
        description="Get the statistics of a GitHub repository."
    )
    parser.add_argument(
        "--name",
        type=str,
        default="PrefectHQ/prefect",
        help="The name of the repository to get the statistics.",
    )
    return parser.parse_args()


def main():
    """Main function to run the flow."""
    # Get args and run the flow
    args = parse_args()
    result = get_repo_info(repo_name=args.name)
    # Log the result
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
