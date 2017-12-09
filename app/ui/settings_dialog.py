from app.properties import write_config
from app.ui.dialogs import show_dialog, DialogType
from . import Gtk


def show_settings_dialog(transient, options):
    SettingsDialog(transient, options)


class SettingsDialog:
    def __init__(self, transient, options):
        handlers = {"on_data_dir_field_icon_press": self.on_data_dir_field_icon_press}
        builder = Gtk.Builder()
        builder.add_objects_from_file("app/ui/dialogs.glade", ("settings_dialog", ))
        builder.connect_signals(handlers)
        self._options = options
        self._dialog = builder.get_object("settings_dialog")
        self._dialog.set_transient_for(transient)
        self._host_field = builder.get_object("host_field")
        self._host_field.set_text(options["host"])
        self._port_field = builder.get_object("port_field")
        self._port_field.set_text(options["port"])
        self._login_field = builder.get_object("login_field")
        self._login_field.set_text(options["user"])
        self._password_field = builder.get_object("password_field")
        self._password_field.set_text(options["password"])
        self._services_field = builder.get_object("services_field")
        self._services_field.set_text(options["services_path"])
        self._user_bouquet_field = builder.get_object("user_bouquet_field")
        self._user_bouquet_field.set_text(options["user_bouquet_path"])
        self._satellites_xml_field = builder.get_object("satellites_xml_field")
        self._satellites_xml_field.set_text(options["satellites_xml_path"])
        self._data_dir_field = builder.get_object("data_dir_field")
        self._data_dir_field.set_text(options["data_dir_path"])

        if self._dialog.run() == Gtk.ResponseType.OK:
            options["host"] = self._host_field.get_text()
            options["port"] = self._port_field.get_text()
            options["user"] = self._login_field.get_text()
            options["password"] = self._password_field.get_text()
            options["services_path"] = self._services_field.get_text()
            options["user_bouquet_path"] = self._user_bouquet_field.get_text()
            options["satellites_xml_path"] = self._satellites_xml_field.get_text()
            options["data_dir_path"] = self._data_dir_field.get_text()
            write_config(options)
        self._dialog.destroy()

    def on_data_dir_field_icon_press(self, entry, icon, event_button):
        response = show_dialog(dialog_type=DialogType.CHOOSER, transient=self._dialog, options=self._options)
        if response != Gtk.ResponseType.CANCEL:
            entry.set_text(response)


if __name__ == "__main__":
    pass
