"""Fix editable_text + config upload

Revision ID: cf51392161db
Revises: 80b65fe0a8d9
Create Date: 2025-07-28 17:47:33.963932
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cf51392161db'
down_revision = '80b65fe0a8d9'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('editable_text', schema=None) as batch_op:
        batch_op.add_column(sa.Column('identifier', sa.String(length=64), nullable=False))
        batch_op.alter_column('content', existing_type=sa.TEXT(), nullable=False)
        batch_op.create_unique_constraint('uq_editable_text_identifier', ['identifier'])  # 👈 fix
        batch_op.drop_column('key')

def downgrade():
    with op.batch_alter_table('editable_text', schema=None) as batch_op:
        batch_op.add_column(sa.Column('key', sa.VARCHAR(length=255), nullable=False))
        batch_op.drop_constraint('uq_editable_text_identifier', type_='unique')  # 👈 fix anche qui
        batch_op.alter_column('content', existing_type=sa.TEXT(), nullable=True)
        batch_op.drop_column('identifier')
