# availability-calcul

Small project used mostly to have something to deploy to GCP.
Will calculate availability for the day/week/month/year given an input of downtime.

## Installation instructions

### Google Cloud Function installation

The file [availability_cloudfunction.py](availability_cloudfunction.py) is ready to deploy to a cloud function
The current version is used as http trigger function and will return json

Deploy by copying the file into GCP console in a new cloud function.
Or deploy with the SDK on condition code is hosted on gcloud repositories ([see doc](https://cloud.google.com/functions/docs/deploying/repo))

```bash
gcloud function deploy <your function name> --region=<REGION> \
--trigger-http --runtime=python37 \
[--entry-point=<function to execute in the deployed file>] \
[--memory=<memory limit>] \
[--source=<https://source.developers.google.com/projects/PROJECT_ID/repos/REPOSITORY_ID/moveable-aliases/master/paths/SOURCE>]
```

See all the option 

```
$ gcloud functions deploy --help
```

#### Usage

Use with this format:

```bash
curl 'https://gcloud-region-project-id.cloudfunctions.net/function_name?downtime=0d5h54m'
OR
curl -X POST -H "Content-Type: application/json" -d '{"downtime":"0d5h54m"}' 'https://gcloud-region-project-id.cloudfunctions.net/function_name'
```
Also possible to filter period :
```bash
curl 'https://gcloud-region-project-id.cloudfunctions.net/function_name?downtime=0d5h54m&period=monthly'
curl -X POST -H "Content-Type: application/json" -d '{"downtime":"0d5h54m", "period":"monthly"}' 'https://gcloud-region-project-id.cloudfunctions.net/function_name'
OR

```

The above will output

```json
{"daily": 75.417, "weekly": 96.488, "monthly": 99.207, "yearly": 99.933}
```

Calculations are made on the current month and year.

### Google AppEngine deployment

TODO

### Docker deployment

TODO

## Unit tests

TODO


## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details
