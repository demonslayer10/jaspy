/*
 * Copyright (C) 2016, Maximilian Koehl <mail@koehlma.de>
 *
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License version 3 as published by
 * the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY
 * WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
 * PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

BaseException.$def('__new__', function (cls, args) {
    BaseException.check_subclass(cls);
    return new PyObject(cls, {'args': pack_tuple(args)})
}, ['*args']);

Exception.$def('__init__', function (self, args) {
    self.setattr('args', pack_tuple(args));
}, ['*args']);