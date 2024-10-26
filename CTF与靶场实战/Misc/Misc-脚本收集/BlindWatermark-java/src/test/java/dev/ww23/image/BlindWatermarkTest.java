/*
 * Copyright (c) 2020 ww23(https://github.com/ww23/BlindWatermark).
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package dev.ww23.image;

import dev.ww23.image.converter.Converter;
import dev.ww23.image.converter.DctConverter;
import dev.ww23.image.converter.DftConverter;
import dev.ww23.image.dencoder.Decoder;
import dev.ww23.image.dencoder.Encoder;
import dev.ww23.image.dencoder.ImageEncoder;
import dev.ww23.image.dencoder.TextEncoder;
import org.bytedeco.javacpp.Loader;
import org.bytedeco.opencv.opencv_java;
import org.junit.jupiter.api.Test;

class BlindWatermarkTest {

    private static final String SRC = "image/gakki-src.png";
    private static final String TEXT_WM = "测试test";
    private static final String IMAGE_WM = "image/watermark.png";

    static {
        Loader.load(opencv_java.class);
    }

    @Test
    void dctImage() {
        Converter converter = new DctConverter();
        Encoder encoder = new ImageEncoder(converter);
        Decoder decoder = new Decoder(converter);
        encoder.encode(SRC, IMAGE_WM, "image/gakki-dct-img-ec.jpg");
        decoder.decode("image/gakki-dct-img-ec.jpg", "image/gakki-dct-img-dc.jpg");
    }

    @Test
    void dctText() {
        Converter converter = new DctConverter();
        Encoder encoder = new TextEncoder(converter);
        Decoder decoder = new Decoder(converter);
        encoder.encode(SRC, TEXT_WM, "image/gakki-dct-text-ec.jpg");
        decoder.decode("image/gakki-dct-text-ec.jpg", "image/gakki-dct-text-dc.jpg");
    }

    @Test
    void dftImage() {
        Converter converter = new DftConverter();
        Encoder encoder = new ImageEncoder(converter);
        encoder.encode(SRC, IMAGE_WM, "image/gakki-dft-img-ec.png");
        Decoder decoder = new Decoder(converter);
        decoder.decode("image/gakki-dft-img-ec.png", "image/gakki-dft-img-dc.png");
    }

    @Test
    void dftText() {
        Converter converter = new DftConverter();
        Encoder encoder = new TextEncoder(converter);
        Decoder decoder = new Decoder(converter);
        encoder.encode(SRC, TEXT_WM, "image/gakki-dft-text-ec.png");
        decoder.decode("image/gakki-dft-text-ec.png", "image/gakki-dft-text-dc.png");
    }

}
