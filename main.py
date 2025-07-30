import sys

major = sys.version_info.major
minor = sys.version_info.minor

if (major, minor) == (3, 12):
    print("Đang chạy Python 3.12")
elif (major, minor) == (3, 11):
    print("Đang chạy Python 3.11")
else:
    print(f"Python version khác: {major}.{minor}")

# Ví dụ này chỉ chạy được trên Python 3.12 trở lên

# Định nghĩa một hàm generic sử dụng cú pháp type parameter mới
# def get_first_element[T](items: list[T]) -> T:
#     if not items:
#         raise ValueError("Danh sách không được rỗng")
#     return items[0]

# # Sử dụng hàm với các kiểu khác nhau
# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5]
#     first_number = get_first_element(numbers)
#     print(f"Phần tử đầu tiên của danh sách số: {first_number}")

#     strings = ["apple", "banana", "cherry"]
#     first_string = get_first_element(strings)
#     print(f"Phần tử đầu tiên của danh sách chuỗi: {first_string}")

#     # Ví dụ với danh sách rỗng (sẽ gây lỗi ValueError)
#     try:
#         empty_list = []
#         get_first_element(empty_list)
#     except ValueError as e:
#         print(f"Lỗi: {e}")



