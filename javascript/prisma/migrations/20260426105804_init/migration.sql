-- CreateTable
CREATE TABLE "BrowserJob" (
    "id" UUID NOT NULL,
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "status" TEXT NOT NULL DEFAULT 'pending',
    "created_at" TIMESTAMPTZ(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ(6),

    CONSTRAINT "BrowserJob_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Browser" (
    "id" UUID NOT NULL,
    "profile_id" UUID NOT NULL,
    "browser_job_id" UUID,
    "name" TEXT NOT NULL,
    "description" TEXT,
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "created_at" TIMESTAMPTZ(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ(6),

    CONSTRAINT "Browser_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Profile" (
    "id" UUID NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT,
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "created_at" TIMESTAMPTZ(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ(6),

    CONSTRAINT "Profile_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Browser_profile_id_key" ON "Browser"("profile_id");

-- CreateIndex
CREATE UNIQUE INDEX "Browser_browser_job_id_key" ON "Browser"("browser_job_id");

-- AddForeignKey
ALTER TABLE "Browser" ADD CONSTRAINT "Browser_profile_id_fkey" FOREIGN KEY ("profile_id") REFERENCES "Profile"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Browser" ADD CONSTRAINT "Browser_browser_job_id_fkey" FOREIGN KEY ("browser_job_id") REFERENCES "BrowserJob"("id") ON DELETE SET NULL ON UPDATE CASCADE;
