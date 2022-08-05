class GitHubQueries:

    get_pull_request_numbers = """
    SELECT 
    id,
    number
    from github.pulls.pull_requests   
    WHERE
    owner = '%s' AND repo = '%s';
    """

    get_open_request_with_cycle_time = """
    SELECT 
    merge_commit_sha, 
    title, 
    updated_at, 
    created_at,
    round(julianday('now') - julianday(created_at)) as issued_days,
    changed_files,  
    number, 
    merged, 
    merged_at,
    state
    from github.pulls.pull_requests   
    WHERE
    owner = '%s' AND repo = '%s'
    AND pull_number = '%s'
    AND merged = False
    AND state = 'open';
    """