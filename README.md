`HNGi Internship`

# Stage One Task

## The  Objective

You are welcome to Stage One of the HNGi Internship! In this task we will be  creating and hosting an API endpoint that accepts GET requests and returns specific information in JSON format. Your objective is to implement this API following the provided requirements.

## Requirements

The task requires you to create an API endpoint that provides the following information in JSON format:

``` text
Slack name
Current day of the week
Current UTC time (with validation of +/-2 minutes)
Track
The GitHub URL of the file being executed
The GitHub URL of the full source code
A status code of 200 (Success)
```

Here's an example of the expected JSON format:

``` json
{
   "slack_name": "example_name",
   "current_day": "Monday",
   "utc_time": "2023-08-21T15:04:05Z",
   "track": "backend",
   "github_file_url": "<https://github.com/username/repo/blob/main/file_name.ext>",
   "github_repo_url": "<https://github.com/username/repo>",
   "status_code": 200
}
```

## Acceptance Criteria

To successfully complete this task, make sure to meet the following criteria:

1. Create a publicly accessible API endpoint.
2. Accept two GET request query parameters: slack_name and track.
3. Ensure that the response includes the slack_name passed as a GET request query parameter.
4. Display the current day of the week in full.
5. Return the current UTC time, accurate within a +/-2 minute window.
6. Display the track based on the "track" GET parameter.

7. Include direct links to the specific GitHub file and the GitHub repository.
8. Return a Status Code of 200 (Success).
9. Ensure the response adheres to the specified JSON format.
10. Thoroughly test the endpoint for accessibility, format, and data correctness before submission.

#Technologies used:
##Python
##Flask

