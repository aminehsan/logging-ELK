# A Python library for interacting with Logstash - ELK

## How to run Python
```bash
logstash_logger = LogstashLogger(host='...', port=..., level='...', project='...', name='...')

logstash_logger.info(msg='...', extra={})
logstash_logger.error(msg='...', extra={})
```

## How to configuration logstash.conf
```bash
if [project_name] == "..." and [logger_name] == "..." {
    elasticsearch {
        hosts => ...
        index => ...
        user => ...
        password => ...
    }
}
```

#### Structure :
```
├── logstash_logger.py
├── requirements.txt
```
