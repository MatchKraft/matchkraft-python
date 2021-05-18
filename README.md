# MatchKraft API for Python

Official Python client for the [MatchKraft API](https://matchkraft.com/api/). Build and run fuzzy matching algorithms for company names from your Python apps.


Installation
---------------


You can use pip to install the library:

```bash
$ pip install matchkraft
```

Alternatively, you can just clone the repository and run the setup.py script:

```bash
$ python setup.py install
```


Usage
------


Before making requests to the API, you need to create an instance of the MatchKraft client. You will have to use your [account API Key](https://app.matchkraft.com/login):

```python
from matchkraft import MatchKraft

# Instantiate the client Using your API key
mk = MatchKraft('<YOUR API TOKEN HERE>')
```

### Create a Highlight Duplicates Job

From the MatchKraft client instance, you can create a higlight duplicates job. Use this type of job if you want to normalize a list of company names.


```python
job_id = mk.highlight_duplicates(name='My Python Final',
primary_list=[
        'WALMART',
        'IKEA',
        'ikea',
        'super che',
        'amazon',
        'wALMART',
        'microsoft',
        'microsof',
        'WAL-MART'
    ]
)

```

### Create a fuzzy match job

If you want to associate company names in two lists, you can use a fuzzy match job.

```python
job_id = mk.fuzzy_match(name='Big Job Two List 5',primary_list=[
        'WALMART',
        'Amazon',
        'Microsof'
    ],secondary_list=[
        'WALMART',
        'Microsoft'
    ])

```

### Execute a Job


You can run your jobs using the job_id generated when you created the job.

```python
mk.execute_job(job_id=job_id)

```

### Retrieve Job Information

You can retrieve a job information using the function: get_results_information.

```python
results = mk.get_results_information(job_id=job_id)
```

The job information object has 5 variables:
<!-- TABLE_GENERATE_START -->

| Fields        | Description   |
| ------------- | ------------- |
| id | GUID of a specific job              |
| name  | Job name  |
| status  | Job status  |
| progress  | Current progress of a job  |
| type  | Fuzzy match or Highlight duplicates  |

<!-- TABLE_GENERATE_END -->

### Retrieve results

You can retrieve all the results with the following code:

```python
results = mk.get_results_information(job_id=job_id)
```

The results object has only two fields:
<!-- TABLE_GENERATE_START -->

| Fields        | Description   |
| ------------- | ------------- |
| master_record | Contains a company name record from your input.              |
| match_record  | Contains a fuzzy match result related to the master record.  |

<!-- TABLE_GENERATE_END -->


### Complete code example

Here is an example to run a fuzzy match job in MatchKraft.

```python
from matchkraft import MatchKraft

mk = MatchKraft('<YOUR API TOKEN HERE>')

job_id = mk.fuzzy_match(name='Big Job Two List 5',primary_list=[
        'WALMARTs',
        'IKEA'
    ],secondary_list=[
        'Amazon',
        'Walmart'
    ])

print (job_id)

# Execute Job Status
mk.execute_job(job_id=job_id)

# Wait till the job is completed
job  = mk.get_job_information(job_id=job_id)
print (job.status)

while (job.status!='Completed'):
       print (job.status)
       time.sleep(10)
       job  = mk.get_job_information(job_id=job_id)

#Show Results
results = mk.get_results_information(job_id=job_id)
if isinstance(results, list):
    for r in results:
        print(r.master_record + ' --> ' + r.match_record)
else:
    print("No Results Found")
```
