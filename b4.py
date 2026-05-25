#1. Phân tích Input / Output
# Input
#     number_of_forms: Số lượng phiếu đăng ký cần nhập, kiểu số nguyên (Integer).
#     registration_data: Chuỗi thông tin thô của từng phiếu (String), phân tách bằng dấu |.
# Output
    # In ra phiếu đăng ký hợp lệ hoặc các thông báo lỗi tương ứng

# Đề xuất giải pháp
# Kiểm tra số lượng: Dùng cấu trúc điều kiện if-else để chặn lỗi ngay từ đầu nếu số lượng phiếu 
# Tách dữ liệu: Sử dụng .split('|') để phân rã chuỗi thông tin thành danh sách các thuộc tính cơ bản
# Định dạng Email: Dùng toán tử not in để kiểm tra sự tồn tại của ký tự @.
# Độ dài Mã học viên: Dùng hàm len() kiểm tra nếu mã ngắn hơn 5 ký tự sẽ coi là không hợp lệ.

# Thuật toán:
# BẮT ĐẦU
#     Nhập 'number_of_forms' và ép kiểu sang Số nguyên
#     NẾU 'number_of_forms' <= 0:
#         In "Số lượng phiếu đăng ký không hợp lệ"
#     NẾU KHÔNG:
#         VÒNG LẶP Duyệt 'i' chạy từ 0 đến 'number_of_forms - 1':
#             Nhập chuỗi 'registration_data' (Họ tên | Khóa học | Mã HV | Email)
#             Tách 'registration_data' bằng dấu '|' thành danh sách 'parts'

#             NẾU số lượng phần tử trong 'parts' khác 4:
#                 In "Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này"
#                 BỎ QUA lượt này (continue)
                
#             Gán và làm sạch dữ liệu:
#                 full_name = parts[0].strip().title()
#                 course_name = parts[1].strip().title()
#                 student_code = parts[2].strip().upper()
#                 email = parts[3].strip().lower()
                
#             NẾU ký tự '@' không nằm trong 'email':
#                 In "Email không hợp lệ. Bỏ qua phiếu này"
#                 BỎ QUA lượt này (continue)
                
#             NẾU độ dài 'student_code' < 5:
#                 In "Mã học viên không hợp lệ. Bỏ qua phiếu này"
#                 BỎ QUA lượt này (continue)
                
#             Khởi tạo confirm_code = (student_code+ "_"+ course_name.upper().replace(" ", "-"))
            
#             In thông tin phiếu đã chuẩn hóa (Học viên, Khóa học, Mã học viên, Email, Mã xác nhận)
# KẾT THÚC

number_of_forms = int(input("Nhập số lượng phiếu đăng ký: "))
if number_of_forms <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:

    for i in range(number_of_forms):

        print(f"\nNhập phiếu đăng ký thứ {i + 1}")

        registration_data = input(
            "Nhập dữ liệu (Họ tên | Khóa học | Mã HV | Email): "
        )

        parts = registration_data.split("|")

        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        full_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue
        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue
        confirm_code = (student_code+ "_"+ course_name.upper().replace(" ", "-"))
        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")

        print("Học viên:", full_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_code)
        print("Email:", email)
        print("Mã xác nhận:", confirm_code)