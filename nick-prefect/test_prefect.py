import httpx
from prefect import flow, task, get_run_logger

@task
def get_url(url: str, params: dict = None):
    """ Get the JSON response from a URL.

    Args:
        url (str): _description_
        params (dict, optional): _description_. Defaults to None.

    Returns:
        Dict: Response JSON
    """
    response = httpx.get(url, params=params)
    response.raise_for_status()
    return response.json()

@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def get_repo_info(
    repo_name: str = "PrefectHQ/prefect"
):
    """ Get the statistics of a GitHub repository.

    Args:
        repo_name (str, optional): _description_. Defaults to "PrefectHQ/prefect".
    """
    # Get the repository information
    url = f"https://api.github.com/repos/{repo_name}"
    repo = get_url(url)
    
    # Log the statistics
    logger = get_run_logger()
    logger.info("PrefectHQ/prefect repository statistics 🤓:")
    logger.info(f"Stars 🌠 : {repo['stargazers_count']}")
    logger.info(f"Forks 🍴 : {repo['forks_count']}")

if __name__ == "__main__":
    get_repo_info()
