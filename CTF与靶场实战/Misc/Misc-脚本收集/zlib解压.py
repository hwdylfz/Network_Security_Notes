import zlib

def decompress_zlib(input_file, output_file):
    try:
        with open(input_file, 'rb') as compressed_file:
            compressed_data = compressed_file.read()
            decompressed_data = zlib.decompress(compressed_data)

        with open(output_file, 'wb') as decompressed_file:
            decompressed_file.write(decompressed_data)

        print(f"成功解压缩文件 '{input_file}' 到 '{output_file}'")
    except Exception as e:
        print(f"解压缩文件时发生错误: {e}")

# 使用示例
input_filename = '29.zlib'  # 替换为实际的文件名
output_filename = 'fuck'  # 替换为你想要保存解压后数据的文件名

decompress_zlib(input_filename, output_filename)
