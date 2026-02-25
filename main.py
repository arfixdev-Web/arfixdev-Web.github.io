from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, RoundedRectangle
import platform

# إعدادات النافذة لتشبه تطبيقات الأجهزة المتطورة
Window.clearcolor = get_color_from_hex('#000814') # أزرق داكن جداً (Deep Space)

class ModernButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0) # شفاف لنرسم خلفية مخصصة
        self.color = get_color_from_hex('#00ffff')
        self.font_size = '18sp'
        self.bold = True
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#003566')) # لون الزر
            RoundedRectangle(pos=self.pos, size=self.size, radius=[15,])

class ArFixPro(App):
    def build(self):
        # الحاوية الرئيسية مع هوامش احترافية
        main_layout = BoxLayout(orientation='vertical', padding=40, spacing=25)

        # شعار علوي بسيط (يمكنك استبداله بصورة لاحقاً)
        self.header = Label(
            text='[b][color=00ffff]ARFIX[/color] PRO[/b]',
            markup=True,
            font_size='45sp',
            size_hint_y=None,
            height=120
        )

        # خط فاصل جمالي
        separator = Label(text='—' * 20, color=get_color_from_hex('#003566'), size_hint_y=None, height=10)

        # شاشة عرض البيانات (Console) بتصميم "الهكر"
        self.display_panel = BoxLayout(orientation='vertical', size_hint_y=0.4)
        with self.display_panel.canvas.before:
            Color(rgba=get_color_from_hex('#001d3d'))
            self.rect = RoundedRectangle(radius=[20,])
        
        self.console_text = Label(
            text='[color=00ff00]> SYSTEM INITIALIZED...[/color]\n[color=808080]Ready for Diagnostics[/color]',
            markup=True,
            font_size='15sp',
            halign='center',
            valign='middle'
        )
        self.display_panel.add_widget(self.console_text)

        # أزرار التحكم
        btn_scan = ModernButton(text="START SYSTEM SCAN")
        btn_scan.bind(on_release=self.run_scan)

        btn_clean = ModernButton(text="OPTIMIZE RECOVERY")
        btn_clean.bind(on_release=self.run_clean)

        # إضافة العناصر للواجهة
        main_layout.add_widget(self.header)
        main_layout.add_widget(separator)
        main_layout.add_widget(self.display_panel)
        main_layout.add_widget(btn_scan)
        main_layout.add_widget(btn_clean)

        return main_layout

    def run_scan(self, instance):
        self.console_text.text = f"[color=00ffff]Scanning: {platform.system()} {platform.machine()}[/color]\n[color=00ff00]Status: SECURE[/color]"

    def run_clean(self, instance):
        self.console_text.text = "[color=ffff00]Optimizing Cache...[/color]\n[color=00ff00]System at Peak Performance![/color]"

if __name__ == '__main__':
    ArFixPro().run()
