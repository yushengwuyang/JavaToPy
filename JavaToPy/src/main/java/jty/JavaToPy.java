package jty;

import org.codehaus.jackson.map.ObjectMapper;
import py4j.ClientServer;

import java.io.IOException;
import java.util.List;

class JavaToPy {

    public String  javatopy(List<Double> list) throws IOException {
        ClientServer clientServer = new ClientServer(null);
        Predict_Proba predict_proba = (Predict_Proba) clientServer.getPythonServerEntryPoint(new Class[] { Predict_Proba.class });
        String re_list = null;
        for(int i =0; i < 1000; i++){
            ObjectMapper objectMapper = new ObjectMapper();
            byte[] bytes = objectMapper.writeValueAsBytes(list);
            re_list = predict_proba.predict_proba1(bytes);
        }
        long times = 0;
        predict_proba.timeclear();
        for(int i =0; i < 1000; i++){
            long start = System.currentTimeMillis();
            ObjectMapper objectMapper = new ObjectMapper();
            byte[] bytes = objectMapper.writeValueAsBytes(list);
            re_list = predict_proba.predict_proba1(bytes);
            char[] list1 = re_list.toCharArray();
            long end = System.currentTimeMillis();
            times += end - start;
        }
        System.out.println(String.format("python平均时间: %fms", (double)predict_proba.timeaverage()));
        System.out.println(String.format("调用接口平均时间： %.3fms", (times / 1000.0)));
        return re_list;
    }
}