import argparse
import json
from pathlib import Path


def solve(data):
    catalog = data["catalog"]
    observations = data["observations"]
    candidates = sorted(catalog)
    traits = set().union(*(set(row) for row in catalog.values()))
    trace = []
    while len(candidates) > 1:
        options = []
        for trait in traits:
            count = sum(trait in catalog[item] for item in candidates)
            balance = min(count, len(candidates) - count)
            if balance and trait in observations:
                options.append((-balance, trait))
        if not options:
            break
        _, trait = min(options)
        answer = observations[trait]
        if type(answer) is not bool:
            raise ValueError("Observations must be true or false")
        candidates = [item for item in candidates if (trait in catalog[item]) == answer]
        trace.append({"question": trait, "answer": answer, "remaining": candidates[:]})
        traits.remove(trait)
    candidates = [item for item in candidates if all((trait in catalog[item]) == answer
                  for trait, answer in observations.items())]
    return {"candidates": candidates, "trace": trace}

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Identify a mystery specimen by asking the most informative available yes/no question.')
    parser.add_argument("input", nargs="?", type=Path, default=Path(__file__).with_name("sample.json"))
    args = parser.parse_args()
    print(json.dumps(solve(json.loads(args.input.read_text())), indent=2))
