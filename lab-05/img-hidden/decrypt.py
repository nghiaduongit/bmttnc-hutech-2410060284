import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    
    # Trích xuất các bit cuối cùng từ mỗi kênh màu
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Chuyển đổi chuỗi nhị phân thành văn bản
    message = ""
    for i in range(0, len(binary_message), 8):
        char_bin = binary_message[i:i+8]
        # Kiểm tra nếu gặp chuỗi đánh dấu kết thúc (trong ảnh gốc ghi chú là \0)
        char = chr(int(char_bin, 2))
        
        # Lưu ý: Code trong ảnh dùng '1111111111111110' làm điểm dừng 
        # nhưng phần giải mã lại kiểm tra ký tự dừng. 
        # Nếu char là ký tự không hợp lệ hoặc theo logic ảnh:
        if char == '\0' or char_bin == '11111111': 
            break
        message += char
        
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()