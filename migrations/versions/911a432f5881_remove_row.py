"""remove row

Revision ID: 911a432f5881
Revises: bfc05cd4cbd8
Create Date: 2019-12-24 14:20:59.409511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '911a432f5881'
down_revision = 'bfc05cd4cbd8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('row')
    with op.batch_alter_table('seat', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('row_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('row_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key(None, 'row', ['row_id'], ['id'])

    op.create_table('row',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('auditorium_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['auditorium_id'], ['auditorium.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
