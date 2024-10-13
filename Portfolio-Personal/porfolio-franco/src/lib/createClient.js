import { createClient } from '@supabase/supabase-js'

const key = import.meta.env.VITE_ANNON_KEY_SUPABAS
const url = import.meta.env.VITE_URL_SUPABASE

export const supabase = createClient(url, key)
