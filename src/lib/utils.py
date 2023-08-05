def parse_ner(
    results: list[dict],
) -> list[dict]:
    for i, r in enumerate(reversed(results)):
        r["score"] = float(r["score"])
        if (
            i + 1 < len(results)
            and r["entity_group"] == results[i + 1]["entity_group"]
            and r["start"] == results[i + 1]["end"]
        ):
            results[i + 1]["end"] = r["end"]
            results[i + 1]["word"] += r["word"]
            results[i + 1]["score"] = max(
                r["score"],
                results[i + 1]["score"],
            )
            r["remove"] = True

    return [r for r in results if not r.get("remove")]
