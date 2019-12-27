"""remove shows from movie

Revision ID: bfc05cd4cbd8
Revises: 6d0b70f6dbb4
Create Date: 2019-12-23 22:14:08.725397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfc05cd4cbd8'
down_revision = '6d0b70f6dbb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('rating',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('runtime',
               existing_type=sa.TIME(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.alter_column('runtime',
               existing_type=sa.TIME(),
               nullable=True)
        batch_op.alter_column('rating',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###
