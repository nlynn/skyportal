"""plans API

Revision ID: 529166dc7732
Revises: 46a40b35cdbb
Create Date: 2022-02-12 20:55:46.665147

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '529166dc7732'
down_revision = '46a40b35cdbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        """
alter type "public"."followup_apis" rename to "followup_apis__old_version_to_be_dropped";

create type "public"."followup_apis" as enum ('KAITAPI', 'SEDMAPI', 'SEDMV2API', 'IOOAPI', 'IOIAPI', 'SPRATAPI', 'SINISTROAPI', 'SPECTRALAPI', 'FLOYDSAPI', 'MUSCATAPI', 'MMAAPI', 'SLACKAPI', 'ZTFAPI', 'ZTFMMAAPI');

alter table "public"."instruments" alter column api_classname type "public"."followup_apis" using api_classname::text::"public"."followup_apis";

alter table "public"."instruments" alter column api_classname_obsplan type "public"."followup_apis" using api_classname_obsplan::text::"public"."followup_apis";

drop type "public"."followup_apis__old_version_to_be_dropped";
"""
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
