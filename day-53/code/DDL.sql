-- =====================================================
-- DATABASE: University Management System
-- Author: S. L. Phani
-- Tables: 30+
-- =====================================================

-- =====================
-- 1. Department Table
-- =====================
CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) UNIQUE NOT NULL,
    building VARCHAR(100),
    budget DECIMAL(12,2) CHECK (budget >= 0)
);

-- =====================
-- 2. Professor Table
-- =====================
CREATE TABLE Professor (
    prof_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL(10,2) CHECK (salary > 0),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- =====================
-- 3. Course Table
-- =====================
CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT CHECK (credits BETWEEN 1 AND 6),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- =====================
-- 4. Student Table
-- =====================
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE,
    gender CHAR(1) CHECK (gender IN ('M','F','O')),
    email VARCHAR(100) UNIQUE,
    admission_year INT CHECK (admission_year >= 2000),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- =====================
-- 5. Enrollment Table
-- =====================
CREATE TABLE Enrollment (
    enrollment_id INT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    semester VARCHAR(20) NOT NULL,
    year INT CHECK (year >= 2000),
    grade CHAR(2),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- =====================
-- 6. ClassRoom Table
-- =====================
CREATE TABLE ClassRoom (
    room_id INT PRIMARY KEY,
    building VARCHAR(50),
    room_number VARCHAR(10),
    capacity INT CHECK (capacity > 0)
);

-- =====================
-- 7. Schedule Table
-- =====================
CREATE TABLE Schedule (
    schedule_id INT PRIMARY KEY,
    course_id INT NOT NULL,
    prof_id INT NOT NULL,
    room_id INT,
    day_of_week VARCHAR(10),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (prof_id) REFERENCES Professor(prof_id),
    FOREIGN KEY (room_id) REFERENCES ClassRoom(room_id)
);

-- =====================
-- 8. Attendance Table
-- =====================
CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    date DATE NOT NULL,
    status VARCHAR(10) CHECK (status IN ('Present', 'Absent', 'Late')),
    FOREIGN KEY (enrollment_id) REFERENCES Enrollment(enrollment_id)
);

-- =====================
-- 9. Library Table
-- =====================
CREATE TABLE Library (
    library_id INT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

-- =====================
-- 10. Book Table
-- =====================
CREATE TABLE Book (
    book_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    isbn VARCHAR(20) UNIQUE,
    publisher VARCHAR(100),
    year_published INT,
    library_id INT,
    FOREIGN KEY (library_id) REFERENCES Library(library_id)
);

-- =====================
-- 11. Book_Issue Table
-- =====================
CREATE TABLE Book_Issue (
    issue_id INT PRIMARY KEY,
    student_id INT NOT NULL,
    book_id INT NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

-- =====================
-- 12. Hostel Table
-- =====================
CREATE TABLE Hostel (
    hostel_id INT PRIMARY KEY,
    name VARCHAR(100),
    capacity INT,
    warden_name VARCHAR(100)
);

-- =====================
-- 13. Room_Allocation Table
-- =====================
CREATE TABLE Room_Allocation (
    allocation_id INT PRIMARY KEY,
    student_id INT,
    hostel_id INT,
    room_no VARCHAR(10),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (hostel_id) REFERENCES Hostel(hostel_id)
);

-- =====================
-- 14. Fee Table
-- =====================
CREATE TABLE Fee (
    fee_id INT PRIMARY KEY,
    student_id INT,
    amount DECIMAL(10,2) CHECK (amount >= 0),
    due_date DATE,
    status VARCHAR(20) CHECK (status IN ('Paid', 'Pending')),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

-- =====================
-- 15. Scholarship Table
-- =====================
CREATE TABLE Scholarship (
    scholarship_id INT PRIMARY KEY,
    name VARCHAR(100),
    amount DECIMAL(10,2),
    eligibility_criteria VARCHAR(255)
);

-- =====================
-- 16. Student_Scholarship Table
-- =====================
CREATE TABLE Student_Scholarship (
    id INT PRIMARY KEY,
    student_id INT,
    scholarship_id INT,
    awarded_date DATE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (scholarship_id) REFERENCES Scholarship(scholarship_id)
);

-- =====================
-- 17. Exam Table
-- =====================
CREATE TABLE Exam (
    exam_id INT PRIMARY KEY,
    course_id INT,
    exam_type VARCHAR(20) CHECK (exam_type IN ('Midterm', 'Final', 'Quiz')),
    exam_date DATE,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- =====================
-- 18. Exam_Result Table
-- =====================
CREATE TABLE Exam_Result (
    result_id INT PRIMARY KEY,
    exam_id INT,
    student_id INT,
    marks_obtained DECIMAL(5,2) CHECK (marks_obtained BETWEEN 0 AND 100),
    FOREIGN KEY (exam_id) REFERENCES Exam(exam_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

-- =====================
-- 19. Club Table
-- =====================
CREATE TABLE Club (
    club_id INT PRIMARY KEY,
    club_name VARCHAR(100),
    faculty_incharge INT,
    FOREIGN KEY (faculty_incharge) REFERENCES Professor(prof_id)
);

-- =====================
-- 20. Club_Members Table
-- =====================
CREATE TABLE Club_Members (
    member_id INT PRIMARY KEY,
    student_id INT,
    club_id INT,
    join_date DATE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (club_id) REFERENCES Club(club_id)
);

-- =====================
-- 21. Event Table
-- =====================
CREATE TABLE Event (
    event_id INT PRIMARY KEY,
    event_name VARCHAR(100),
    club_id INT,
    event_date DATE,
    location VARCHAR(100),
    FOREIGN KEY (club_id) REFERENCES Club(club_id)
);

-- =====================
-- 22. Research_Project Table
-- =====================
CREATE TABLE Research_Project (
    project_id INT PRIMARY KEY,
    title VARCHAR(150),
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12,2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- =====================
-- 23. Project_Member Table
-- =====================
CREATE TABLE Project_Member (
    id INT PRIMARY KEY,
    project_id INT,
    prof_id INT,
    role VARCHAR(50),
    FOREIGN KEY (project_id) REFERENCES Research_Project(project_id),
    FOREIGN KEY (prof_id) REFERENCES Professor(prof_id)
);

-- =====================
-- 24. Transport Table
-- =====================
CREATE TABLE Transport (
    bus_id INT PRIMARY KEY,
    route_name VARCHAR(100),
    driver_name VARCHAR(100),
    capacity INT
);

-- =====================
-- 25. Bus_Pass Table
-- =====================
CREATE TABLE Bus_Pass (
    pass_id INT PRIMARY KEY,
    student_id INT,
    bus_id INT,
    valid_from DATE,
    valid_to DATE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (bus_id) REFERENCES Transport(bus_id)
);

-- =====================
-- 26. Inventory Table
-- =====================
CREATE TABLE Inventory (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100),
    quantity INT CHECK (quantity >= 0),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Department(dept_id)
);

-- =====================
-- 27. Vendor Table
-- =====================
CREATE TABLE Vendor (
    vendor_id INT PRIMARY KEY,
    name VARCHAR(100),
    contact_no VARCHAR(15),
    email VARCHAR(100)
);

-- =====================
-- 28. Purchase_Order Table
-- =====================
CREATE TABLE Purchase_Order (
    order_id INT PRIMARY KEY,
    vendor_id INT,
    order_date DATE,
    total_amount DECIMAL(12,2),
    FOREIGN KEY (vendor_id) REFERENCES Vendor(vendor_id)
);

-- =====================
-- 29. Order_Details Table
-- =====================
CREATE TABLE Order_Details (
    detail_id INT PRIMARY KEY,
    order_id INT,
    item_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES Purchase_Order(order_id),
    FOREIGN KEY (item_id) REFERENCES Inventory(item_id)
);

-- =====================
-- 30. Alumni Table
-- =====================
CREATE TABLE Alumni (
    alumni_id INT PRIMARY KEY,
    student_id INT,
    grad_year INT,
    current_company VARCHAR(100),
    designation VARCHAR(100),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

-- =====================
-- 31. Placement Table
-- =====================
CREATE TABLE Placement (
    placement_id INT PRIMARY KEY,
    company_name VARCHAR(100),
    salary_package DECIMAL(10,2),
    job_role VARCHAR(100),
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

-- =====================
-- 32. Feedback Table
-- =====================
CREATE TABLE Feedback (
    feedback_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments VARCHAR(255),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- =====================
-- 33. Login_Credentials Table
-- =====================
CREATE TABLE Login_Credentials (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) CHECK (role IN ('Student', 'Professor', 'Admin'))
);

-- =====================
-- 34. Audit_Log Table
-- =====================
CREATE TABLE Audit_Log (
    log_id INT PRIMARY KEY,
    user_id INT,
    action VARCHAR(100),
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Login_Credentials(user_id)
);

-- =====================
-- 35. Notifications Table
-- =====================
CREATE TABLE Notifications (
    notification_id INT PRIMARY KEY,
    user_id INT,
    message VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_read BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES Login_Credentials(user_id)
);
