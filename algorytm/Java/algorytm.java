import java.util.Arrays;

public class Main{

	public static void main(Stringp[] args) {
		int[] test1 = {3, 5, -2, 2, 1, 8, 15};

		System.out.println(algorytm(test1));
	}

	public int algorytm(int[] array) {
		int smallest = 1;

		Arrays.sort(array);

		if (array[array.length-1] <= smallest) {
			return smallest;
		}

		for (int i = 0; i < array.length; i++) {
			if (array[i] > smallest) {
				return smallest;
			}
			else if (array[i] == smallest) {
				smallest++;
			}
		}

		return smallest;
	}
}