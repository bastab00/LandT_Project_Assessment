def ranking_leaderboard(data):
    avgs = []

    for sid, info in data["students"].items():
        raw_scores = info.get("scores", {})

        scores = [v for v in raw_scores.values() if isinstance(v, int)]

        if scores:
            avg = sum(scores) / len(scores)
            avgs.append((sid, info["name"], avg))

    if not avgs:
        print("No valid scores available.")
        return

    avgs.sort(key=lambda x: x[2], reverse=True)

    print("\nLeaderboard:")
    for i, (sid, name, avg) in enumerate(avgs, start=1):
        print(f"{i}. {sid} - {name}: {avg:.2f}")
