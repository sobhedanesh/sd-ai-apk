import os
from kivy.app import App
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout

# کدهای مخفی‌سازی نوار وضعیت حذف شدند تا ساعت و باتری دیده شوند.

class WebViewApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        if platform == 'android':
            # فراخوانی وب‌ویو بومی اندروید
            from jnius import autoclass
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            
            activity = PythonActivity.mActivity
            webview = WebView(activity)
            
            # فعال‌سازی دسترسی‌های پردازشی وب‌سایت
            webview.getSettings().setJavaScriptEnabled(True)
            webview.getSettings().setDomStorageEnabled(True)
            webview.setWebViewClient(WebViewClient())
            
            # بارگذاری آدرس سایت شما
            webview.loadUrl('https://sobhedanesh.github.io/h-s-c-2')
            
            activity.setContentView(webview)
        else:
            from kivy.uix.label import Label
            return Label(text="این نسخه مخصوص اندروید است.\nبرای تست در کامپیوتر از فایل preview.py استفاده کنید.")
            
        return layout

if __name__ == '__main__':
    WebViewApp().run()