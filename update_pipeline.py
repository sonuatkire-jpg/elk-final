#!/usr/bin/env python3
"""
Push / update the Logstash pipeline in Elasticsearch Centralized Pipeline Management.
Usage:
    python update_pipeline.py
"""
import os
import json
from datetime import datetime, timezone

from elasticsearch import Elasticsearch


# ---- Configuration ----
ES_HOST = os.getenv("ES_HOST", "https://my-deployment-1cb05e.es.ap-south-1.aws.elastic-cloud.com:443")
ES_USER = os.getenv("ES_USER", "logstash")
ES_PASSWORD = os.getenv("ES_PASSWORD", "logstash")
PIPELINE_ID = os.getenv("PIPELINE_ID", "bank_pipeline")
PIPELINE_FILE = os.getenv("PIPELINE_FILE", "pipelines/bank_pipeline.conf")
# -----------------------


def load_pipeline(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def push_pipeline(es: Elasticsearch, pipeline_id: str, pipeline_text: str) -> dict:
    """
    Store the pipeline in the .logstash index used by Centralized Pipeline Management.
    """
    doc = {
        "pipeline": pipeline_text,
        "description": f"Pipeline {pipeline_id} - last updated {datetime.now(timezone.utc).isoformat()}",
        "last_modified": datetime.now(timezone.utc).isoformat(),
        "username": ES_USER
    }

    # Centralized Pipeline Management stores docs in .logstash/pipelines/<id>
    response = es.index(index=".logstash", id=pipeline_id, document=doc)
    return response


def verify_pipeline(es: Elasticsearch, pipeline_id: str) -> dict:
    try:
        return es.get(index=".logstash", id=pipeline_id)
    except Exception as e:
        return {"error": str(e)}


def main():
    print(f"Connecting to Elasticsearch: {ES_HOST}")
    es = Elasticsearch([ES_HOST], basic_auth=(ES_USER, ES_PASSWORD), verify_certs=True)

    try:
        ping_ok = es.ping()
    except Exception as e:
        print(f"Ping error: {type(e).__name__}: {e}")
        ping_ok = False
    if not ping_ok:
        raise ConnectionError("Could not ping Elasticsearch. Check credentials / host.")
    print("Connection OK")

    pipeline_text = load_pipeline(PIPELINE_FILE)
    print(f"Loaded pipeline from {PIPELINE_FILE} ({len(pipeline_text)} chars)")

    print(f"Pushing pipeline '{PIPELINE_ID}' to Elasticsearch ...")
    resp = push_pipeline(es, PIPELINE_ID, pipeline_text)
    print(f"Index response: {json.dumps(resp.body if hasattr(resp, 'body') else resp, indent=2)}")

    print("Verifying stored pipeline ...")
    verify = verify_pipeline(es, PIPELINE_ID)
    if "error" in verify:
        print(f"Verification failed: {verify['error']}")
    else:
        print(f"Pipeline '{PIPELINE_ID}' found in index .logstash")
        print(f"  Version: {verify.get('_version')}")
        print(f"  Description: {verify.get('_source', {}).get('description')}")

    print("Done. Logstash will pick up the updated pipeline on its next poll (every 5s).")


if __name__ == "__main__":
    main()
