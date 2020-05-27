# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class HlswebcamPlugin(octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin,
                      octoprint.plugin.TemplatePlugin):

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			# put your plugin's default settings here
		)

	##~~ AssetPlugin mixin

	def get_assets(self):
		return dict(
			js=["js/hlswebcam.js","js/hls.js"],
			css=["css/hlswebcam.css"]
		)

	def get_template_configs(self):
		return [
			dict(type="tab", template="hlswebcam_tab.jinja2", replaces="control", name="Control")
		]

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			hlswebcam=dict(
				displayName="HLS Webcam",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-HLSWebcam",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-HLSWebcam/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "HLS Webcam"
__plugin_pythoncompat__ = ">=2.7,<4" # python 2 and 3

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = HlswebcamPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

