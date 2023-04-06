from odoo import api, fields, models


class Subject(models.Model):
    """
    Clase Subject parte del modulo education, crea el modelo school_subject
    """
    _name = "school.subject"
    _description = "Detalles del curso"
    _inherit = ["mail.thread", "mail.activity.mixin"]  # Modelos de mail

    name = fields.Char(string="Nombre del curso", required=True, tracking=True)
    credits = fields.Integer(string="Creditos del curso", required=True, tracking=True)
    max_students = fields.Integer(
        string="Maximo de estudiantes", required=True, tracking=True
    )
    active = fields.Boolean(string="Activo", default=True, required=True, tracking=True)
    student_ids = fields.Many2many(
        "school.student", string="Estudiantes", required=True, tracking=True
    )
    teacher_id = fields.Many2one(
        "school.teacher", string="Profesor", required=True, tracking=True
    )

    @api.constrains("credits")
    def check_credits(self):
        """
        Verifica que los creditos no sean negativos
        """
        for record in self:
            if record.credits < 0:
                raise models.ValidationError("Los créditos no pueden ser negativos")

    @api.constrains("max_students")
    def check_max_students(self):
        """
        Verifica que el maximo de estudiantes no sea negativo
        """
        for record in self:
            if record.max_students < 0:
                raise models.ValidationError(
                    "La cantidad de alumnos no puede ser negativa"
                )
