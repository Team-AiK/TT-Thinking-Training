function solution(clothes) {
  const catagories = {};
  let multi = 1;

  clothes.forEach( x => {
    if (x[1] in catagories) {
      catagories[x[1]] += 1
    }
    else {
      catagories[x[1]] = 1
    }
  });

  const len = Object.keys(catagories).length;
  if (len === clothes.length || len === 1) {
    return clothes.length
  }
  else {
    for (const key in catagories) {
      multi *= catagories[key];
    }
    return clothes.length + multi;
  }
}

console.log(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]));