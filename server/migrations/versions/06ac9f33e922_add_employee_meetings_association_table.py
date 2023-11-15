"""add employee_meetings association table

Revision ID: 06ac9f33e922
Revises: bc7f39195868
Create Date: 2023-11-14 16:57:01.199286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06ac9f33e922'
down_revision = 'bc7f39195868'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees_meetings',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employees_meetings_employee_id_employees')),
    sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], name=op.f('fk_employees_meetings_meeting_id_meetings')),
    sa.PrimaryKeyConstraint('employee_id', 'meeting_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees_meetings')
    # ### end Alembic commands ###
