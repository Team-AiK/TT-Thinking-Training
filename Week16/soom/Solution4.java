import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class Solution {

	ArrayList<Integer> ans = new ArrayList<Integer>();
	HashMap<Integer, Integer> pMap = new HashMap<Integer, Integer>();

	public int[] solution(String[] genres, int[] plays) {

		HashMap<Integer, String> gMap = new HashMap<Integer, String>();
		HashMap<String, Integer> gen = new HashMap<String, Integer>();

		List<Integer> indexArr = new ArrayList<Integer>();

		for (int i = 0; i < genres.length; i++) {
			gMap.put(i, genres[i]);
			pMap.put(i, plays[i]);
			if (gen.containsKey(genres[i])) {
				gen.put(genres[i], gen.get(genres[i]) + plays[i]);
			} else {
				gen.put(genres[i], plays[i]);
			}
		}

		Iterator it = sortByValue(gen).iterator();

		while (it.hasNext()) {
			String temp = (String) it.next();
			int index = 0;

			for (String gMapValue : gMap.values()) {
				if (gMapValue.equals(temp)) {
					indexArr.add(index);
				}
				index++;
			}

			getBest(indexArr);

			indexArr.clear();
		}

		int[] answer = new int[ans.size()];

		for (int j = 0; j < ans.size(); j++) {
			answer[j] = ans.get(j);
		}

		return answer;
	}

	// value값으로 내림차순 정렬
	public static List sortByValue(final Map map) {

		List<String> list = new ArrayList();

		list.addAll(map.keySet());

		Collections.sort(list, new Comparator<Object>() {

			public int compare(Object o1, Object o2) {
				Object v1 = map.get(o1);
				Object v2 = map.get(o2);
				return ((Comparable) v2).compareTo(v1);
			}

		});

		return list;

	}

	public void getBest(List<Integer> arr) {
		int max1 = pMap.get(arr.get(0)), max2 = 0, temp = 0, index1 = arr.get(0), index2 = 0;

		if (arr.size() > 1) {
			for (int i = 1; i < arr.size(); i++) {
				if (pMap.get(arr.get(i)) > max1) {
					temp = pMap.get(arr.get(i));
					max2 = max1;
					max1 = temp;

					index2 = index1;
					index1 = arr.get(i);
				} else if (pMap.get(arr.get(i)) > max2) {
					max2 = pMap.get(arr.get(i));
					index2 = arr.get(i);
				}
			}

			ans.add(index1);
			ans.add(index2);
		} else {
			ans.add(arr.get(0));
		}
	}
}