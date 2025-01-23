import { createClient } from '@hey-api/openapi-ts';
import defineConfig from './openapi.config.ts';

createClient(defineConfig);