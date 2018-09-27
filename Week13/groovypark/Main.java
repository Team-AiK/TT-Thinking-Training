package groovypark;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        Game game = new Game(N, K);
        System.out.println(game.getMinTime());
        br.close();
    }
    static class Game {
        private int N, K;
        private int[] visited;

        Game(int n, int k) {
            N = n;
            K = k;
            visited = new int[100001];
        }

        int getMinTime() {
            Arrays.fill(visited, -1);
            visited[N] = 0;
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(N);

            while (!queue.isEmpty()) {
                //noinspection ConstantConditions
                int soovin = queue.poll();
                if (soovin == K) {
                    return visited[soovin];
                }

                if (soovin-1 >= 0 && visited[soovin-1] == -1) {
                    visited[soovin-1] = visited[soovin] + 1;
                    queue.offer(soovin-1);
                }

                if (soovin+1 <= 100000 && visited[soovin+1] == -1) {
                    visited[soovin+1] = visited[soovin] + 1;
                    queue.offer(soovin+1);
                }

                if (soovin*2 <= 100000 && visited[soovin*2] == -1) {
                    visited[soovin*2] = visited[soovin] + 1;
                    queue.offer(soovin*2);
                }
            }
            return -1;
        }
    }
}
