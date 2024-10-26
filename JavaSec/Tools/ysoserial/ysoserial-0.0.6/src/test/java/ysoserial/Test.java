package ysoserial;

import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class Test {

    public static void main(String[] args) throws Exception {
        ObjectInputStream os = new ObjectInputStream(new FileInputStream("src/test/java/ysoserial/dnslog1.ser"));
        os.readObject();
        System.out.println("OK");
    }
}

