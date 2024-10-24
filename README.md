# A Python library for interacting with Logstash - ELK

## How to run Python
```bash
logger = Logstash(host='...', port=..., project='...', name='...')

logger.info(msg='...', extra={})
logger.error(msg='...', extra={})
```

## How to configuration logstash.conf
```bash
if [project] == "..." and [logger_name] == "..." {
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
├── main.py
├── requirements.txt
```
