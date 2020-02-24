package jty;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Demo {
    public static void main(String[] args) throws IOException {
        List<Double> list = new ArrayList<>();
        Random r = new Random();

        for(int i =0; i <200; i++ ){
            list.add(r.nextDouble());
        }

        JavaToPy javaToPy = new JavaToPy();
        javaToPy.javatopy(list);
        return;
    }

}
