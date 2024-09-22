/*
* */

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

/*
* System.out.println()
* Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);
* Arrays.stream(graph).forEach(System.out::println);
* */


public class Main {
    static List<List<Integer>> combs = new ArrayList<>();

    static void comb(int start, Stack<Integer> stack) {

        if(stack.size() == 2) {
            combs.add(new ArrayList<>(stack));
            return;
        }

        for(int i=start; i < 3; i++) {
            stack.add(i);
            comb(i+1, stack);
            stack.pop();
        }
    }

    static void perm(Stack<Integer> stack) {
        if(stack.size() == m) {
            perms.add(new ArrayList<>(stack));
            return;
        }

        for(int i=0; i<n; i++) {
            if(use[i] == false) {
                use[i] = true;
                stack.add(i);
                perm(stack);
                stack.pop();
                use[i] = false;
            }
        }
    }

    static boolean[] use;
    static List<List<Integer>> perms = new ArrayList<>();
    static int n;
    static int m;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        use = new boolean[n+1];

        Stack<Integer> stack = new Stack<>();
        perm(stack);
        System.out.println(perms);

        List<Integer> l = new ArrayList<>();
        l.add(2);

        List<Integer> l2 = new ArrayList<>(l);

        l.add(3);

        System.out.println(l);
        System.out.println(l2);
    }
}
