# 1️⃣ استيراد مكتبة CSV هذه المكتبة مسؤولة عن:
# قراءة ملفات CSV
# الكتابة فيها
import csv

# 2️⃣ فتح ملف الكتب للقراءة
# r" يمنع مشاكل المسار في ويندوز
with open(r"C:\Users\Acer\Downloads\Bestseller - Sheet1.csv",
          'r',
          encoding='utf-8'
) as file:
# 3️⃣ إنشاء قارئ CSV
    csv_reader = csv.reader(file)
# 4️⃣ قراءة صف العناوين ,و next(): يجيب أول سطر فقط و غالباً هي العناوين , لاننا نحتاج عامود المبيعات
    header = next(csv_reader)

# # نبحث عن عمود المبيعات
    sales_index = None
    for i, column in enumerate(header):
        if 'sales' in column.lower():
            sales_index = i
            break

    best_selling_book = None
    highest_sales = 0

    for row in csv_reader:
        sales = float(row[sales_index])

        if sales > highest_sales:
            highest_sales = sales
            best_selling_book = row

with open('bestseller_info.csv', 'w', newline='', encoding='utf-8') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(header)
    csv_writer.writerow(best_selling_book)
