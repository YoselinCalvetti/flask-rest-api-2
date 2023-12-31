"""empty message

Revision ID: 3d573807f0a6
Revises: 8feac0b71202
Create Date: 2023-09-01 12:22:38.983425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d573807f0a6'
down_revision = '8feac0b71202'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('height', sa.String(length=120), nullable=False),
    sa.Column('mass', sa.String(length=120), nullable=False),
    sa.Column('hair_color', sa.String(length=120), nullable=False),
    sa.Column('skin_color', sa.String(length=120), nullable=False),
    sa.Column('eye_color', sa.String(length=120), nullable=False),
    sa.Column('birth_year', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('birth_year'),
    sa.UniqueConstraint('eye_color'),
    sa.UniqueConstraint('gender'),
    sa.UniqueConstraint('hair_color'),
    sa.UniqueConstraint('height'),
    sa.UniqueConstraint('mass'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('skin_color')
    )
    op.drop_table('personajes')
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('people_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('favoritos_personajes_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'people', ['people_id'], ['id'])
        batch_op.drop_column('personajes_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('personajes_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favoritos_personajes_id_fkey', 'personajes', ['personajes_id'], ['id'])
        batch_op.drop_column('people_id')

    op.create_table('personajes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('height', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('mass', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('hair_color', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('skin_color', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('eye_color', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('birth_year', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='personajes_pkey'),
    sa.UniqueConstraint('birth_year', name='personajes_birth_year_key'),
    sa.UniqueConstraint('eye_color', name='personajes_eye_color_key'),
    sa.UniqueConstraint('gender', name='personajes_gender_key'),
    sa.UniqueConstraint('hair_color', name='personajes_hair_color_key'),
    sa.UniqueConstraint('height', name='personajes_height_key'),
    sa.UniqueConstraint('mass', name='personajes_mass_key'),
    sa.UniqueConstraint('name', name='personajes_name_key'),
    sa.UniqueConstraint('skin_color', name='personajes_skin_color_key')
    )
    op.drop_table('people')
    # ### end Alembic commands ###
