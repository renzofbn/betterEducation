from odoo import fields, models


class Teacher(models.Model):
    """
    Clase Teacher parte del modulo education, crea el modelo school_teacher
    """

    _name = "school.teacher"
    _description = "Datos del instructor"
    _inherit = ["mail.thread", "mail.activity.mixin"]  # Modelos de mail

    name = fields.Char(string="Nombre del instructor", required=True, tracking=True)
    profile = fields.Text(string="Perfil del instructor", required=True, tracking=True)
    subject_ids = fields.One2many(
        "school.subject", "teacher_id", string="Cursos", tracking=True
    )
