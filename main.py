class Student:
	listStudents = [{
		'id': '1',
		'name': 'Hung',
		'class': 'a1',
		'age': 'nam',
		'medium score': '5'
	}, {
		'id': '2',
		'name': 'thang',
		'class': 'a3',
		'age': 'nam',
		'medium score': '6'
	}, {
		'id': '3',
		'name': 'hong',
		'class': 'a3',
		'age': 'nam',
		'medium score': '9'
	}]

	def addStudent(self):
		"""Hàm thêm một sinh viên"""
		print("*** THÊM SINH VIÊN ***")

		# Cấu trúc lưu trữ một sinh viên
		infor = {
			'id': '',
			'name': '',
			'class': '',
			'age': '',
			'medium score': ''
		}

		# Nhập ID, có kiểm tra trùng ID thì nhập lại
		print("Nhập ID sinh viên:")
		infor['id'] = input()

		# Nhập tên
		print("Nhập tên sinh viên:")
		infor['name'] = input()

		print("Nhập lớp của sinh viên:")
		infor['class'] = input()

		print("Nhập gioi tinh sinh viên:")
		infor['age'] = input()

		print("Nhập  điểm TB sinh viên:")
		infor['medium score'] = input()

		# Lưu vào danh sách sv
		self.listStudents.append(infor)

	def findStudent(self, id):
		"""Hàm tìm một sinh viên"""
		for i in range(0, len(self.listStudents)):
			if self.listStudents[i]['id'] == id:
				# Trả về mảng gồm 2 phần tử,
				# 0 là vị trí tìm thấy và 1 là dữ liệu
				return [i, self.listStudents[i]]
		return False

	def deleteStudent(self):
		"""Hàm xóa sih viên"""
		print("*** XÓA SINH VIÊN ***")
		print("Nhập ID sinh viên cần xóa:")
		id = input()

		student = self.findStudent(id)

		if student != False:
			self.listStudents.remove(student[1])
			print("Xóa sinh viên thành công")
		else:
			print("Không tìm thấy sinh viên cần xóa")

	def showStudents(self):
		"""Hàm hiển thị danh sách sv"""
		print("*** DANH SÁCH SINH VIÊN HIỆN TẠI ***")
		for i in range(0, len(self.listStudents)):
			print("[", self.listStudents[i]['id'], "]", "[", self.listStudents[i]['name'], "]", )

student = Student()

action = 0

while action >= 0:
	if action == 1:
		student.addStudent()
	elif action == 2:
		student.deleteStudent()
	elif action == 3:
		student.showStudents()

	print("Chọn chức năng muốn thực hiện:")
	print("Nhập 1: Thêm sinh viên")
	print("Nhập 2: Xóa sinh viên")
	print("Nhập 3: Xem danh sách sinh viên")
	print("Nhập 0: Thoát khỏi chương trình")
	action = int(input())
	if action == 0:
		break





