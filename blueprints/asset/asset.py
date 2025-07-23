from flask import Blueprint, render_template

asset = Blueprint("asset", static_folder="static", template_folder="templates")

asset.route("")
