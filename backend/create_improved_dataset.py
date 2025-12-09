# ============================================
# TẠO DATASET MẪU CHẤT LƯỢNG CAO
# Create High-Quality Sample Dataset
# ============================================

import pandas as pd
from pathlib import Path
import random

# ============================================
# DỮ LIỆU MẪU - SAMPLE DATA
# ============================================

# Mỗi topic có 20 câu khác nhau, sẽ kết hợp tạo 200 bài
# Each topic has 20 different sentences, will combine to create 200 articles

SAMPLE_SENTENCES = {
    'Thể thao': [
        'Đội tuyển Việt Nam giành chiến thắng ấn tượng với tỷ số 3-0 trước đối thủ.',
        'Các cầu thủ đã thể hiện phong độ tuyệt vời và tinh thần chiến đấu cao trong trận đấu.',
        'Huấn luyện viên Park Hang-seo rất hài lòng với kết quả này và khen ngợi học trò.',
        'Giải bóng đá ngoại hạng Anh diễn ra hấp dẫn với nhiều trận cầu đỉnh cao cuối tuần qua.',
        'Manchester City đang dẫn đầu bảng xếp hạng với lối chơi tấn công ấn tượng.',
        'Liverpool và Arsenal cũng đang có phong độ rất tốt trong những trận gần đây.',
        'Cristiano Ronaldo ghi bàn thắng quyết định giúp đội nhà giành trọn ba điểm.',
        'Lionel Messi tiếp tục thể hiện đẳng cấp siêu sao với pha kiến tạo bàn thắng đẹp mắt.',
        'Olympic Paris 2024 hứa hẹn sẽ là một kỳ đại hội thể thao đầy hấp dẫn.',
        'Vận động viên Việt Nam đang tích cực tập luyện chuẩn bị cho SEA Games sắp tới.',
        'Rafael Nadal vô địch giải quần vợt Pháp mở rộng sau trận chung kết kịch tính.',
        'Usain Bolt được tôn vinh là vận động viên điền kinh vĩ đại nhất mọi thời đại.',
        'Các đội bóng châu Âu đang săn đón tài năng trẻ từ Việt Nam và Đông Nam Á.',
        'World Cup 2026 sẽ được tổ chức tại Mỹ Canada và Mexico với quy mô lớn chưa từng có.',
        'Giải võ thuật UFC thu hút hàng triệu người hâm mộ trên toàn thế giới theo dõi.',
        'Nguyễn Thị Ánh Viên phá kỷ lục quốc gia ở nội dung bơi 200m tự do.',
        'Thể thao điện tử esports đang ngày càng phát triển và được công nhận rộng rãi.',
        'Các câu lạc bộ bóng đá Việt Nam đầu tư mạnh để nâng cao chất lượng đội hình.',
        'Giải marathon quốc tế thu hút hơn 10 nghìn vận động viên tham gia cuối tuần qua.',
        'Đội tuyển bóng chuyền nữ Việt Nam vào chung kết sau chiến thắng nghẹt thở.',
    ],
    
    'Kinh tế':  [
        'Nền kinh tế Việt Nam tăng trưởng ấn tượng trong quý đầu năm đạt mức 6.5 phần trăm.',
        'Xuất khẩu và đầu tư nước ngoài đều có sự tăng trưởng tích cực trong thời gian qua.',
        'Chính phủ đang triển khai nhiều chính sách hỗ trợ doanh nghiệp vượt qua khó khăn.',
        'Thị trường chứng khoán Việt Nam biến động mạnh trong tuần qua do yếu tố quốc tế.',
        'VN-Index giảm xuống mức thấp nhất trong hai tháng qua khiến nhà đầu tư lo lắng.',
        'Nhiều cổ phiếu ngân hàng và bất động sản bị bán tháo mạnh trong phiên giao dịch.',
        'Giá vàng trong nước tăng cao do ảnh hưởng từ thị trường vàng thế giới biến động.',
        'Ngân hàng Nhà nước công bố giảm lãi suất để hỗ trợ doanh nghiệp và người dân.',
        'Doanh nghiệp khởi nghiệp Việt Nam nhận được nhiều vốn đầu tư từ quỹ nước ngoài.',
        'Thương mại điện tử phát triển mạnh mẽ với doanh thu tăng trưởng hai con số.',
        'Giá dầu thế giới tăng cao ảnh hưởng đến chi phí vận tải và sản xuất trong nước.',
        'Các tập đoàn lớn công bố kế hoạch mở rộng đầu tư tại Việt Nam trong năm tới.',
        'Lạm phát được kiểm soát tốt nhờ các biện pháp điều tiết của chính phủ hiệu quả.',
        'Hội nghị thượng đỉnh kinh tế APEC mở ra nhiều cơ hội hợp tác cho doanh nghiệp.',
        'Ngành du lịch phục hồi mạnh mẽ với lượng khách quốc tế tăng gấp ba lần.',
        'Sản xuất công nghiệp tăng trưởng tốt nhờ đơn hàng xuất khẩu tăng cao.',
        'Các dự án hạ tầng giao thông được đẩy mạnh để thúc đẩy phát triển kinh tế.',
        'Thị trường bất động sản có dấu hiệu hạ nhiệt sau thời gian tăng nóng.',
        'Đồng tiền Việt Nam ổn định trước các biến động của thị trường ngoại hối.',
        'Xuất khẩu nông sản đạt kỷ lục với giá trị hơn 50 tỷ đô la Mỹ.',
    ],
    
    'Giải trí': [
        'Ca sĩ nổi tiếng vừa ra mắt album mới với nhiều bản hit được khán giả yêu thích.',
        'Album đạt vị trí số một trên các bảng xếp hạng âm nhạc chỉ sau một tuần phát hành.',
        'Buổi họp báo ra mắt album thu hút đông đảo báo chí và người hâm mộ tham dự.',
        'Bộ phim điện ảnh Việt Nam vừa đoạt giải thưởng tại liên hoan phim quốc tế.',
        'Đạo diễn và diễn viên rất xúc động khi nhận giải thưởng danh giá này.',
        'Phim được đánh giá cao về nội dung sâu sắc và kỹ thuật dựng phim xuất sắc.',
        'Concert của ban nhạc nổi tiếng bán hết vé chỉ sau vài phút mở bán.',
        'Hàng nghìn người hâm mộ xếp hàng từ sáng sớm để mua vé xem show diễn.',
        'Chương trình truyền hình thực tế mới thu hút đông đảo khán giả theo dõi.',
        'Các thí sinh thể hiện tài năng đa dạng từ ca hát đến múa và diễn xuất.',
        'Nghệ sĩ Việt Nam giành giải cao tại cuộc thi tài năng châu Á uy tín.',
        'MV ca nhạc mới đạt 10 triệu lượt xem chỉ sau 24 giờ đăng tải.',
        'Liên hoan phim Việt Nam tổ chức thành công với hơn 100 tác phẩm tham gia.',
        'Diễn viên trẻ gây ấn tượng với vai diễn đầu tay trong phim điện ảnh.',
        'Gameshow hài hước mang đến tiếng cười cho khán giả mỗi cuối tuần.',
        'Nhạc sĩ tài năng sáng tác ca khúc về tình yêu quê hương đất nước.',
        'Triển lãm nghệ thuật đương đại thu hút hàng nghìn người yêu mỹ thuật.',
        'Các ngôi sao điện ảnh tham dự lễ trao giải với trang phục lộng lẫy.',
        'Sân khấu kịch nói trình diễn vở kịch cổ điển với dàn diễn viên tài năng.',
        'Liveshow âm nhạc mang đến không gian nghệ thuật đẳng cấp quốc tế.',
    ],
    
    'Công nghệ': [
        'Trí tuệ nhân tạo AI đang thay đổi nhiều ngành công nghiệp trên toàn thế giới.',
        'Các ứng dụng AI ngày càng phổ biến trong đời sống hàng ngày của người dân.',
        'Việt Nam cũng bắt đầu ứng dụng AI vào nhiều lĩnh vực khác nhau một cách hiệu quả.',
        'Apple vừa ra mắt iPhone thế hệ mới với nhiều tính năng đột phá và ấn tượng.',
        'Sản phẩm được trang bị chip xử lý mạnh mẽ và camera chất lượng cao vượt trội.',
        'Người dùng Việt Nam rất quan tâm và mong chờ sản phẩm công nghệ mới này.',
        'Google phát triển công nghệ tìm kiếm bằng giọng nói tiếng Việt chính xác hơn.',
        'Microsoft đầu tư mạnh vào điện toán đám mây cloud computing tại khu vực.',
        'Samsung mở trung tâm nghiên cứu phát triển công nghệ 5G tại Việt Nam.',
        'Xe điện Tesla được nhiều người quan tâm nhờ công nghệ tự lái tiên tiến.',
        'Blockchain và tiền điện tử đang tạo ra cuộc cách mạng trong lĩnh vực tài chính.',
        'Công nghệ sinh trắc học vân tay và nhận diện khuôn mặt ngày càng phổ biến.',
        'Internet vạn vật IoT kết nối các thiết bị thông minh trong gia đình.',
        'Drone bay không người lái được ứng dụng trong nông nghiệp và giao hàng.',
        'Thực tế ảo VR và thực tế tăng cường AR mở ra trải nghiệm giải trí mới.',
        'Chip xử lý thế hệ mới tăng hiệu suất gấp đôi so với thế hệ trước.',
        'Mạng 5G triển khai rộng rãi với tốc độ truyền tải dữ liệu siêu nhanh.',
        'Robot và tự động hóa thay thế lao động trong các nhà máy sản xuất.',
        'An ninh mạng cyber security trở thành ưu tiên hàng đầu của doanh nghiệp.',
        'Máy in 3D tạo ra các sản phẩm với độ chính xác cao trong y tế và công nghiệp.',
    ],
    
    'Giáo dục': [
        'Bộ Giáo dục và Đào tạo công bố phương án thi tốt nghiệp THPT mới cho năm học tới.',
        'Kỳ thi sẽ có nhiều thay đổi so với năm trước để phù hợp hơn với thực tế.',
        'Học sinh và giáo viên đang tích cực chuẩn bị cho kỳ thi quan trọng sắp tới.',
        'Các trường đại học lớn công bố điểm chuẩn xét tuyển năm nay tăng cao.',
        'Điểm chuẩn của nhiều ngành tăng do số lượng thí sinh đăng ký rất đông.',
        'Thí sinh cần cân nhắc kỹ lựa chọn nguyện vọng để có cơ hội trúng tuyển cao.',
        'Chương trình giáo dục phổ thông mới được áp dụng trên toàn quốc.',
        'Học sinh được học nhiều kỹ năng mềm và tư duy phản biện hơn trước.',
        'Giáo viên tham gia các khóa bồi dưỡng để nâng cao năng lực sư phạm.',
        'Học bổng du học được trao cho học sinh có thành tích xuất sắc.',
        'Các trường quốc tế mở rộng quy mô đào tạo chương trình song ngữ.',
        'Công nghệ số được ứng dụng mạnh mẽ trong giảng dạy và học tập.',
        'Lớp học trực tuyến ngày càng phổ biến nhờ nền tảng công nghệ hiện đại.',
        'Thi Olympic các môn học tìm kiếm học sinh có năng khiếu đặc biệt.',
        'Giáo dục hướng nghiệp giúp học sinh chọn đúng con đường tương lai.',
        'Thư viện điện tử cung cấp hàng nghìn tài liệu học tập miễn phí cho sinh viên.',
        'Các trường đại học hợp tác quốc tế mở chương trình liên kết đào tạo chất lượng cao.',
        'Học phí được hỗ trợ cho học sinh nghèo vượt khó học giỏi.',
        'Cuộc thi khoa học kỹ thuật dành cho học sinh THPT thu hút nhiều dự án sáng tạo.',
        'Giáo dục kỹ năng sống được đưa vào chương trình học chính thức tại trường.',
    ],
    
    'Sức khỏe': [
        'Bộ Y tế khuyến cáo người dân cần tiêm vaccine phòng ngừa dịch bệnh đầy đủ.',
        'Vaccine đã được chứng minh là an toàn và có hiệu quả phòng bệnh rất cao.',
        'Các trung tâm y tế đang tổ chức tiêm chủng rộng rãi miễn phí cho cộng đồng.',
        'Chế độ ăn uống lành mạnh rất quan trọng để duy trì sức khỏe tốt mỗi ngày.',
        'Nên ăn nhiều rau xanh và trái cây tươi giàu vitamin mỗi ngày.',
        'Hạn chế thức ăn nhiều dầu mỡ và đường để tránh béo phì và bệnh tim mạch.',
        'Tập thể dục đều đặn giúp cơ thể khỏe mạnh và tinh thần sảng khoái.',
        'Yoga và thiền định giúp giảm stress và cân bằng tâm lý hiệu quả.',
        'Ngủ đủ giấc từ 7 đến 8 tiếng mỗi đêm rất quan trọng cho sức khỏe.',
        'Khám sức khỏe định kỳ giúp phát hiện bệnh sớm và điều trị kịp thời.',
        'Bác sĩ khuyến cáo người già nên uống đủ nước và vận động nhẹ nhàng.',
        'Thuốc kháng sinh chỉ nên dùng khi có chỉ định của bác sĩ chuyên khoa.',
        'Ung thư có thể phòng ngừa bằng lối sống lành mạnh và khám sàng lọc.',
        'Tim mạch là nguyên nhân gây tử vong hàng đầu cần được quan tâm phòng ngừa.',
        'Đái tháo đường kiểm soát tốt bằng chế độ ăn và thuốc điều trị đúng cách.',
        'Sức khỏe tâm thần cần được chú ý giống như sức khỏe thể chất.',
        'Trẻ em cần được tiêm chủng đầy đủ theo lịch của Bộ Y tế khuyến cáo.',
        'Y học cổ truyền kết hợp y học hiện đại mang lại hiệu quả điều trị tốt.',
        'Bệnh viện đầu tư trang thiết bị y tế hiện đại phục vụ chẩn đoán và điều trị.',
        'Chăm sóc sức khỏe răng miệng đều đặn giúp phòng ngừa sâu răng và nha chu.',
    ],
    
    'Pháp luật': [
        'Bộ luật hình sự được sửa đổi bổ sung nhiều điều khoản mới quan trọng.',
        'Hình phạt đối với tội phạm ma túy và tham nhũng được tăng nặng hơn trước.',
        'Luật sư cho rằng đây là bước tiến quan trọng trong cải cách tư pháp.',
        'Tòa án xét xử vụ án tham nhũng lớn liên quan đến nhiều quan chức.',
        'Bị cáo bị cáo buộc tham ô hàng trăm tỷ đồng tiền của nhà nước.',
        'Phiên tòa diễn ra công khai với sự theo dõi chặt chẽ của dư luận xã hội.',
        'Luật giao thông mới quy định phạt nặng với người vi phạm nồng độ cồn.',
        'Cảnh sát giao thông tăng cường kiểm tra xử lý vi phạm trong dịp lễ.',
        'Quyền và nghĩa vụ của công dân được quy định rõ ràng trong hiến pháp.',
        'Luật bảo vệ quyền lợi người tiêu dùng giúp người dân đòi quyền lợi khi bị lừa.',
        'Tòa án nhân dân giải quyết tranh chấp dân sự theo quy định của pháp luật.',
        'Luật đất đai được sửa đổi để phù hợp với tình hình phát triển kinh tế.',
        'Hợp đồng lao động cần được ký kết đầy đủ để bảo vệ quyền lợi người lao động.',
        'Vi phạm bản quyền tác giả bị xử phạt hành chính hoặc truy cứu hình sự.',
        'Luật doanh nghiệp tạo điều kiện thuận lợi cho khởi nghiệp và đầu tư.',
        'An ninh mạng được bảo vệ bằng luật an toàn thông tin nghiêm ngặt.',
        'Tội phạm công nghệ cao ngày càng tinh vi cần có biện pháp đấu tranh mạnh.',
        'Hòa giải viên giúp giải quyết mâu thuẫn trong cộng đồng một cách hòa bình.',
        'Luật hôn nhân gia đình bảo vệ quyền lợi của phụ nữ và trẻ em trong gia đình.',
        'Trách nhiệm bồi thường thiệt hại được quy định rõ ràng trong luật dân sự.',
    ],
    
    'Thời sự': [
        'Thủ tướng Chính phủ chủ trì họp bàn về kế hoạch phát triển kinh tế năm tới.',
        'Các bộ ngành báo cáo tình hình thực hiện nhiệm vụ trong năm vừa qua đầy đủ.',
        'Chính phủ đặt mục tiêu tăng trưởng cao và bền vững cho đất nước trong tương lai.',
        'Bão lớn đổ bộ vào miền Trung gây thiệt hại nặng nề về người và của cải.',
        'Chính quyền địa phương đã sơ tán dân đến nơi an toàn trước khi bão đến.',
        'Lực lượng cứu hộ đang khẩn trương tìm kiếm người mất tích sau bão lũ.',
        'Quốc hội thảo luận về dự án luật quan trọng liên quan đến đời sống nhân dân.',
        'Đại biểu Quốc hội đóng góp nhiều ý kiến xây dựng cho dự thảo luật mới.',
        'Chủ tịch nước tiếp đón nguyên thủ quốc gia nước bạn thăm chính thức Việt Nam.',
        'Hai bên ký kết nhiều thỏa thuận hợp tác trong các lĩnh vực kinh tế văn hóa.',
        'Hội nghị cấp cao ASEAN bàn về an ninh và phát triển khu vực.',
        'Việt Nam đóng góp tích cực vào các vấn đề chung của cộng đồng quốc tế.',
        'Lễ kỷ niệm ngày Quốc khánh được tổ chức long trọng tại Thủ đô Hà Nội.',
        'Người dân cả nước hân hoan đón mừng ngày lễ lớn của dân tộc.',
        'Chính phủ ban hành nghị định hỗ trợ người dân vùng lũ lụt thiên tai.',
        'Cuộc bầu cử đại biểu Quốc hội diễn ra dân chủ và đúng quy định pháp luật.',
        'Công an triệt phá đường dây buôn bán ma túy lớn xuyên quốc gia.',
        'Hội nghị báo chí công bố thông tin về các chính sách mới của chính phủ.',
        'Đoàn đại biểu cấp cao thăm và làm việc tại các địa phương trọng điểm.',
        'Chương trình từ thiện mang Tết đến với người nghèo vùng sâu vùng xa.',
    ],
    
    'Khoa học': [
        'Các nhà khoa học phát hiện ra loài virus mới có khả năng lây lan rất nhanh.',
        'Nghiên cứu đang được tiến hành để tìm ra vaccine phòng ngừa hiệu quả cao.',
        'Cộng đồng quốc tế hợp tác chặt chẽ trong việc nghiên cứu khoa học y học.',
        'Kính viễn vọng không gian James Webb gửi về những hình ảnh vũ trụ tuyệt đẹp.',
        'Các nhà khoa học đang phân tích dữ liệu để tìm hiểu về nguồn gốc vũ trụ.',
        'Những phát hiện mới có thể thay đổi quan điểm về sự hình thành thiên hà.',
        'Năng lượng mặt trời được nghiên cứu để thay thế nhiên liệu hóa thạch.',
        'Pin lithium thế hệ mới có mật độ năng lượng cao hơn gấp nhiều lần.',
        'Robot thám hiểm sao Hỏa gửi về dữ liệu quý giá về hành tinh đỏ.',
        'Khoa học khí hậu cảnh báo về tác động của biến đổi khí hậu toàn cầu.',
        'Gen chỉnh sửa CRISPR mở ra khả năng chữa trị các bệnh di truyền hiểm nghèo.',
        'Nghiên cứu tế bào gốc giúp tái tạo mô và cơ quan bị tổn thương.',
        'Vật lý lượng tử nghiên cứu các hiện tượng vi mô kỳ lạ của tự nhiên.',
        'Máy tính lượng tử có khả năng xử lý thông tin nhanh hơn máy tính thường.',
        'Hóa học sinh học nghiên cứu các quá trình sống ở cấp độ phân tử.',
        'Khảo cổ học phát hiện di tích nền văn minh cổ đại dưới đáy biển.',
        'Thiên văn học tìm thấy hành tinh mới có khả năng tồn tại sự sống.',
        'Công nghệ nano ứng dụng trong y học điều trị ung thư hiệu quả.',
        'Sinh học biển nghiên cứu hệ sinh thái san hô đang bị đe dọa.',
        'Toán học ứng dụng giải quyết các bài toán tối ưu trong kinh tế và công nghệ.',
    ],
    
    'Văn hóa': [
        'Lễ hội truyền thống đầu xuân được tổ chức tại nhiều địa phương trên cả nước.',
        'Người dân tham gia các hoạt động văn hóa dân gian phong phú đa dạng sắc màu.',
        'Lễ hội là dịp để gìn giữ và phát huy bản sắc văn hóa dân tộc Việt Nam.',
        'Bảo tàng mỹ thuật tổ chức triển lãm tranh của các họa sĩ nổi tiếng trong nước.',
        'Các tác phẩm nghệ thuật thể hiện phong cách độc đáo và sáng tạo ấn tượng.',
        'Triển lãm thu hút đông đảo người yêu nghệ thuật đến tham quan và chiêm ngưỡng.',
        'Di sản văn hóa thế giới được UNESCO công nhận và bảo tồn cẩn thận.',
        'Các công trình kiến trúc cổ kính đại diện cho nền văn minh lâu đời.',
        'Làng nghề truyền thống duy trì và phát triển nghề thủ công mỹ nghệ.',
        'Nghệ nhân đào tạo thế hệ trẻ để giữ gìn kỹ năng làm nghề gia truyền.',
        'Sách văn học Việt Nam được dịch ra nhiều thứ tiếng trên thế giới.',
        'Nhà văn Việt Nam giành giải thưởng văn học quốc tế danh giá.',
        'Ca trù và tuồng là những loại hình nghệ thuật truyền thống độc đáo.',
        'Nghệ sĩ biểu diễn các tiết mục truyền thống phục vụ khán giả trong nước và quốc tế.',
        'Ẩm thực Việt Nam nổi tiếng với hương vị đặc trưng và đa dạng phong phú.',
        'Món phở Việt Nam được bình chọn là một trong những món ăn ngon nhất thế giới.',
        'Tết Nguyên Đán là dịp lễ quan trọng nhất trong năm của người Việt.',
        'Gia đình sum họp cúng tổ tiên và chúc Tết nhau trong không khí ấm áp.',
        'Áo dài Việt Nam là trang phục truyền thống thanh lịch và duyên dáng.',
        'Múa rối nước là nghệ thuật biểu diễn độc đáo chỉ có ở Việt Nam.',
    ],
}

# ============================================
# HÀM TẠO DATASET
# ============================================

def create_article(topic, num_sentences=3):
    """
    Tạo 1 bài viết bằng cách kết hợp ngẫu nhiên các câu
    Create 1 article by randomly combining sentences
    """
    sentences = random.sample(SAMPLE_SENTENCES[topic], min(num_sentences, len(SAMPLE_SENTENCES[topic])))
    return ' '.join(sentences)


def create_dataset(samples_per_topic=200):
    """
    Tạo dataset đầy đủ
    Create full dataset
    """
    print("📝 Đang tạo dataset chất lượng cao...\n")
    
    all_data = []
    
    for topic in SAMPLE_SENTENCES.keys():
        print(f"   📂 {topic}:  Đang tạo {samples_per_topic} bài...")
        
        for i in range(samples_per_topic):
            # Mỗi bài có 3-5 câu ngẫu nhiên
            num_sentences = random.randint(3, 5)
            article = create_article(topic, num_sentences)
            
            all_data.append({
                'text': article,
                'topic':  topic
            })
        
        print(f"   ✅ {topic}:  Hoàn thành {samples_per_topic} bài\n")
    
    df = pd.DataFrame(all_data)
    
    # Shuffle
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return df


def save_dataset(df, output_file='data/improved_dataset.csv'):
    """
    Lưu dataset
    Save dataset
    """
    # Tạo thư mục
    Path('data').mkdir(exist_ok=True)
    
    # Lưu
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print("="*60)
    print(f"\n💾 Đã lưu dataset tại:  {output_file}")
    print(f"📊 Tổng số mẫu: {len(df)}")
    print(f"\n📊 Phân bố theo topic:")
    print(df['topic'].value_counts().to_string())


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print()
    print("╔" + "═"*58 + "╗")
    print("║" + " TẠO DATASET MẪU CHẤT LƯỢNG CAO ".center(58) + "║")
    print("╚" + "═"*58 + "╝")
    print()
    
    # Tạo dataset
    df = create_dataset(samples_per_topic=200)
    
    # Lưu
    save_dataset(df)
    
    print()
    print("="*60)
    print("✅ HOÀN THÀNH!   DATASET CHẤT LƯỢNG CAO ĐÃ SẴN SÀNG!")
    print("="*60)
    print(f"\n📊 Dataset:  2000 bài (200 bài/topic)")
    print(f"💾 File: data/improved_dataset.csv")
    print()
    print("➡️ Tiếp theo: Sửa train_model.py")
    print("   INPUT_FILE = 'data/improved_dataset.csv'")
    print("   Sau đó chạy:  python train_model.py")