class UploadedFileInvalidExtension(Exception):
    @staticmethod
    def message():
        return "فرمت فایل آپلود شده غیرمجاز است"

class UploadedFileInvalidSizeRange(Exception):
    @staticmethod
    def message():
        return "حجم فایل آپلود شده در بازه‌ی مناسب قرار ندارد"
