extends Control

@onready var setting_panel: Panel = $SettingPanel
@onready var bgm_slider: HSlider = $SettingPanel/BGMSlider
@onready var sfx_slider: HSlider = $SettingPanel/SFXSlider

func _ready() -> void:
	bgm_slider.value = SoundManager.get_music_volume() * 100
	sfx_slider.value = SoundManager.get_sound_volume() * 100

func _on_setting_button_pressed() -> void:
	setting_panel.visible = !setting_panel.visible
	bgm_slider.value = SoundManager.get_music_volume() * 100
	sfx_slider.value = SoundManager.get_sound_volume() * 100
	SoundManager.play_button_click_sfx()

func _on_sfx_slider_value_changed(value:float) -> void:
	SoundManager.set_sound_volume(value / 100)

func _on_bgm_slider_value_changed(value:float) -> void:
	SoundManager.set_music_volume(value / 100)

func _on_setting_button_mouse_entered() -> void:
	SoundManager.play_button_hover_sfx()