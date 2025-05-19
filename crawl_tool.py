import requests
from bs4 import BeautifulSoup

# Hàm crawl trang web và lấy thông tin
def crawl_page(url):
    try:
        # Gửi yêu cầu HTTP GET đến trang web
        response = requests.get(url)
        
        # Kiểm tra nếu yêu cầu thành công
        if response.status_code == 200:
            print(f"Đang thu thập dữ liệu từ: {url}")
            
            # Parse nội dung HTML bằng BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Lấy tiêu đề trang
            title = soup.title.string if soup.title else "Không tìm thấy tiêu đề"
            print(f"Tiêu đề trang: {title}")
            
            # Lấy tất cả các liên kết trên trang
            links = soup.find_all('a', href=True)
            print(f"Tổng số liên kết trên trang: {len(links)}")

            # In ra các liên kết
            for link in links:
                print(f"Liên kết: {link['href']}")

        else:
            print(f"Không thể tải trang. Mã lỗi: {response.status_code}")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {str(e)}")

# URL của trang web cần thu thập dữ liệu
url = 'https://www.notion.so/T-NG-H-P-AIRDROP-2025-176115d9378880bbb374d2ff44484697'

# Gọi hàm crawl
crawl_page(url)
