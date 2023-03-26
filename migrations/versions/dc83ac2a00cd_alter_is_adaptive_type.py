"""alter is_adaptive type

Revision ID: dc83ac2a00cd
Revises: 5b50faa6f642
Create Date: 2023-03-27 00:01:07.333213

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dc83ac2a00cd'
down_revision = '5b50faa6f642'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('claims', 'is_adaptive',
               existing_type=sa.BOOLEAN(),
               type_=sa.Text(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('claims', 'is_adaptive',
               existing_type=sa.Text(),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    # ### end Alembic commands ###