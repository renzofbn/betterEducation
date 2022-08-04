from odoo import api, fields, models


class Student(models.Model):
    """
    Clase Student parte del modulo education, crea el modelo school_student
    """
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']   # Modelos de mail
    _description = 'Datos del estudiante'

    name = fields.Char(string='Nombre del estudiante', required=True, tracking=True)
    birth_date = fields.Date(string='Fecha de nacimiento', required=True, tracking=True)
    age = fields.Integer(compute='_compute_age', string='Edad', readonly=True)
    final_exam_grade = fields.Float(string='Nota final', required=True, tracking=True)
    subject_ids = fields.Many2many('school.subject', string='Cursos', tracking=True)   
    
    @api.depends('birth_date')
    def _compute_age(self):
        """
        Calcula la edad del estudiante basandose en su fecha de nacimiento
        """
        for record in self:
            if record.birth_date:
                record.age = fields.Date.from_string(fields.Date.today()).year - fields.Date.from_string(record.birth_date).year
                record.age -= 1 if (fields.Date.from_string(record.birth_date).month, fields.Date.from_string(record.birth_date).day) > (fields.Date.from_string(fields.Date.today()).month, fields.Date.from_string(fields.Date.today()).day) else 0
            else:
                record.age = 0
    

    @api.constrains('birth_date')
    def check_birth_date(self):
        """
        Verifica que la fecha de nacimiento no sea mayor a la actual
        """
        for record in self:
            # Es posible hacer esto, ya que la función se ejecuta al presionar el botón de guardar
            if record.age < 3:
                raise models.ValidationError('El estudiante debe tener 3 años o mas')


    @api.constrains('final_exam_grade')
    def check_final_grade(self):
        """
        Verifica que la nota final este entre 0 y 20
        """
        for record in self:
            if record.final_exam_grade < 0 or record.final_exam_grade > 20:
                raise models.ValidationError('La nota final debe estar entre 0 y 20')