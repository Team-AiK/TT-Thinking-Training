function solution(participant, completion) {
  let hash = new Map();
  for (const p of completion) {
    if (!hash.has(p)) {
      hash.set(p, 1);
    } else {
      hash.set(p, hash.get(p) + 1)
    }
  }

  for (const p of participant) {
    if (!(hash.has(p))) {
      return p;
    } else {
      if (hash.get(p) === 0) {
        return p;
      } else {
        hash.set(p, hash.get(p) - 1);
      }
    }
  }
}

console.log(solution(["kiki", "kiki", "eden"], ["eden", "kiki"]));