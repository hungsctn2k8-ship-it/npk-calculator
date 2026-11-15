def tinh_ti_le_npk(khoi_luong_n, khoi_luong_p2o5, khoi_luong_k2o, tong_khoi_luong):
    """
    Hàm tính phần trăm hàm lượng dinh dưỡng N, P2O5, K2O trong tổng khối lượng phân bón.
    """
    if tong_khoi_luong <= 0:
        return 0, 0, 0
        
    phan_tram_n = (khoi_luong_n / tong_khoi_luong) * 100
    phan_tram_p = (khoi_luong_p2o5 / tong_khoi_luong) * 100
    phan_tram_k = (khoi_luong_k2o / tong_khoi_luong) * 100
    
    return round(phan_tram_n, 1), round(phan_tram_p, 1), round(phan_tram_k, 1)

def main():
    print("--- CHƯƠNG TRÌNH TÍNH TỈ LỆ DINH DƯỠNG PHÂN BÓN NPK ---")
    try:
        tong_kl = float(input("Nhập tổng khối lượng hỗn hợp phân bón (kg): "))
        kl_n = float(input("Nhập khối lượng Nitơ nguyên chất (N) (kg): "))
        kl_p = float(input("Nhập khối lượng Phốt pho oxit (P2O5) (kg): "))
        kl_k = float(input("Nhập khối lượng Kali oxit (K2O) (kg): "))
        
        if kl_n + kl_p + kl_k > tong_kl:
            print("\n[Lỗi] Tổng khối lượng các chất thành phần không thể lớn hơn tổng khối lượng hỗn hợp!")
            return
            
        n, p, k = tinh_ti_le_npk(kl_n, kl_p, kl_k, tong_kl)
        print(f"\n=> Kết quả tỉ lệ N-P-K của mẫu phân bón là: {n} - {p} - {k}")
        print(f"Công thức phân bón tương ứng: NPK {int(n)}-{int(p)}-{int(k)}")

    except ValueError:
        print("\n[Lỗi] Vui lòng chỉ nhập số dữ liệu hợp lệ.")

if __name__ == "__main__":
    main()
